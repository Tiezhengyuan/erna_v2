from django.test import TestCase
from ddt import ddt, data, unpack
from commons.models import User
from sample.models import Sample

@ddt
class TestSamples(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            user_name="tester",
            email="a@abc.com",
            password="pass"
        )
        Sample.objects.create(
            batch_name='batch1',
            sample_name='sample1',
            creator=self.user
        )

    def test_CRUD(self):

        res = Sample.objects.get(batch_name='batch1')
        assert str(res) == 'batch1_sample1'
        assert res.batch_name == 'batch1'
        assert res.sample_name == 'sample1'
        assert res.metadata == None

        res = [ i.sample_name for i in Sample.objects.all()]
        assert res == ['sample1']
        
        res = Sample.objects.filter(batch_name='batch1')\
            .update(sample_name='sample2')
        assert res == 1

        res = Sample.objects.filter(batch_name='batch1').delete()
        assert res[0] == 1
        res = Sample.objects.filter(batch_name='batch1').delete()
        assert res[0] == 0

    def test_unique(self):
        res = Sample.objects.get(batch_name='batch1',
            sample_name='sample1')
        assert str(res) == 'batch1_sample1'
        assert res.metadata is None

        res = Sample.objects.create(
            batch_name='batch1',
            sample_name='sample2',
            creator=self.user
        )
        assert str(res) == 'batch1_sample2'

        res = Sample.objects.create(
            batch_name='batch2',
            sample_name='sample1',
            creator=self.user
        )
        assert str(res) == 'batch2_sample1'

        res = Sample.objects.create(
            batch_name='batch1',
            sample_name='sample1',
            creator=self.user,
            metadata = 'data'
        )
        assert res.metadata == 'data'
    
    @data(
        ['batch1', True],
        ['batch2', False],
    )
    @unpack
    def test_batch_exists(self, input, expect):
        res = Sample.objects.batch_exists(input)
        assert res == expect

    @data(
        ['sample1', True],
        ['sample2', False],
    )
    @unpack
    def test_sample_exists(self, input, expect):
        res = Sample.objects.sample_exists('batch1', input)
        assert res == expect


    @data(
        ['batch1', ['sample1']],
        ['batch2', []],
    )
    @unpack
    def test_get_sample_names_by_batch(self, input, expect):
        res = Sample.objects.get_sample_names_by_batch(input)
        assert res == expect

    @data(
        ['tester', {'batch1': ['sample1']}],
    )
    @unpack
    def test_get_sample_names_by_user(self, input, expect):
        res = Sample.objects.get_sample_names_by_user(input)
        assert res == expect

    def test_load_samples(self):
        samples = [
            {'batch_name':'batch1', 'sample_name': 'sample2'},
            {'batch_name':'batch1', 'sample_name': 'sample3', 'medata':{}},
            {'batch_name':'batch1', 'sample_name': 'sample4', 'medata':{'a':4}},
        ]
        res = Sample.objects.load_samples('tester', samples)
        assert res == 3
    
    @data(
        ['sample1', 'sample2', 'sample2'],
        ['sample1', 'sample1', None],
        ['wrong', 'sample1', None],
    )
    @unpack
    def test_update_sample_name(self, old_name, new_name, expect):
        res = Sample.objects.update_sample_name('batch1', old_name, new_name)
        if expect:
            assert res.sample_name == expect
        else:
            assert res == expect

    @data(
        ['sample1', 1],
        ['wrong', 0],
    )
    @unpack
    def test_delete_sample(self, sample_name, expect):
        res = Sample.objects.delete_sample('batch1', sample_name)
        assert res[0] == expect

    @data(
        ['batch1', 2],
        ['wrong', 0],
    )
    @unpack
    def test_delete_batch_samples(self, batch_name, expect):
        Sample.objects.create(
            batch_name='batch1',
            sample_name='sample2',
            creator=self.user
        )
        res = Sample.objects.delete_batch_samples(batch_name)
        assert res[0] == expect

    @data(
        ['batch1', [None, 'abc']],
        ['wrong', []],
    )
    @unpack
    def test_export_batch(self, batch_name, expect):
        Sample.objects.create(
            batch_name='batch1',
            sample_name='sample2',
            creator=self.user,
            metadata = 'abc'
        )
        res = Sample.objects.export_batch(batch_name)
        assert [i['metadata'] for i in res.values()] == expect

    def test_export_batch(self):
        res = Sample.objects.get_batch_names()
        assert res == {'batch1',}
        
        Sample.objects.create(
            batch_name='batch1',
            sample_name='sample2',
            creator=self.user,
            metadata = 'abc'
        )
        res = Sample.objects.get_batch_names()
        assert res == {'batch1',}

        Sample.objects.create(
            batch_name='batch2',
            sample_name='sample2',
            creator=self.user,
            metadata = 'abc'
        )
        res = Sample.objects.get_batch_names()
        assert res == {'batch1', 'batch2'}
