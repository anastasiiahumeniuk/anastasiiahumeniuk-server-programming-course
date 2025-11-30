class BaseRepository(object):
    model = None

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def delete(self, pk):
        obj = self.get_by_id(pk)
        if not obj:
            return False
        obj.delete()
        return True