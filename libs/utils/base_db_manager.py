from libs.app_logger import AppLogger
from django.db import connection
from libs.sql_helper import dictfetchall, namedtuplefetchall

logger = AppLogger(tag="Base DB Manager")


class BaseDBManager:
    model = None
    has_active_filter = True

    def get_object(self, **filters):
        if "active" not in filters and self.has_active_filter:
            filters["active"] = True

        try:
            obj = self.model.objects.get(**filters)
            logger.info(f"{self.model} found : %s" % obj)
            return obj
        except self.model.DoesNotExist:
            logger.info(f"{self.model} not found in DB")
            return None
        except Exception as e:
            logger.error(e)
            return None

    def get_object_without_active_check(self, **filters):
        try:
            obj = self.model.objects.get(**filters)
            logger.info(f"{self.model} found : %s" % obj)
            return obj
        except self.model.DoesNotExist:
            logger.info(f"{self.model} not found in DB")
            return None
        except Exception as e:
            logger.error(e)
            return None

    def get_object_by_id(self, obj_id):

        logger.info(f"Get {self.model} by id, id: {obj_id}")
        return self.model.objects.get(id=obj_id)

    def list_objects(self, apply_default_active_filter=True, select_for_update=False, get_first=False, **filters):
        if "active" not in filters and self.has_active_filter and apply_default_active_filter:
            filters["active"] = True

        if select_for_update:
            objs = self.model.objects.select_for_update().filter(**filters)
        else:
            objs = self.model.objects.filter(**filters)

        logger.info(f"{self.model} objects found: {objs}")
        if not objs.exists():
            return objs
        elif objs.count() == 1 and get_first:
            return objs.first()
        else:
            return objs

    def create_object(self, **data):
        obj = self.model.objects.create(**data)
        logger.info(f"Create {self.model} {obj}")
        return obj

    # f1f886615dda4443a9529beb97422a13
    def update_objects(self, updates, query):
        query.update(**updates)
        return

    def bulk_update_obj(self, obj, **updates):
        for key, value in updates.items():
            setattr(obj, key, value)
        obj.save()

    def update_object_by_id(self, obj_id, **updates):
        query = self.model.objects.filter(id=obj_id)
        query.update(**updates)
        return query.first()

    def update_object_by_bulk_ids(self, obj_ids, **updates):
        query = self.model.objects.filter(id__in=obj_ids)
        query.update(**updates)
        return query.first()

    def create_in_bulk(self, data, batch_size=300):
        """
        data: List of dictionaries
        """
        payload = [self.model(**vals) for vals in data]
        obj = self.model.objects.bulk_create(payload, batch_size=batch_size)
        logger.info(f"Bulk Create {self.model} {obj}")
        return obj

    def get_or_create(self, defaults={}, **data):
        obj, flag = self.model.objects.get_or_create(**data, defaults=defaults)
        logger.info(f"Get or Create {self.model} {obj}")
        return obj

    def execute_query(self, query):

        objs = self.model.objects.raw(query)

        return objs

    def execute_query_through_cursor(self, query):
        results = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = dictfetchall(cursor)
        return results

    def execute_query_through_cursor_named_tuple(self, query):
        results = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = namedtuplefetchall(cursor)
        return results
