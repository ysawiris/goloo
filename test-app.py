from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app

sample_inventory_id = ObjectId('5d55cffc4a3d4031f42827a2')
sample_inventory = {
    'restroom_name': 'Make School',
    'restroom_gender' : 'All Gender Restroom',
    'pic_path' : '/static/makeschool.jpeg',
    'restroom_price' : 'FREE'
}
sample_inventory_form_data = {
    'restroom_name': sample_inventory['restroom_name'],
    'restroom_gender' : sample_inventory['restroom_gender'],
    'pic_path' : sample_inventory['pic_path'],
    'restroom_price' : sample_inventory['restroom_price']
}

sample_comment_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_comment = {
    'title': 'Test Title',
    'name': 'Test Name',
    'content': 'Test Content',
    'inventory_id' : ObjectId('5d55cffc4a3d4031f42827a2')
}
sample_form_data = {
    'title': sample_comment['title'],
    'name': sample_comment['name'],
    'content': sample_comment['content'],
    'inventory_id': sample_comment['inventory_id']
}

class ContractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    
    def test_index(self):
        """Test the GoLoo homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Restroom', result.data)
    
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_inventory(self, mock_find):
        mock_find.return_value = sample_inventory

        result = self.client.get(f'/restrooms/{sample_inventory_id}')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Make', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_comment(self, mock_find):
        mock_find.return_value = sample_comment

        result = self.client.get(f'/restrooms/{sample_inventory_id}/comments/{sample_comment_id}/edit')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'Title', result.data)

    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_comment(self, mock_update):
        result = self.client.post(f'/restrooms/{sample_inventory_id}/comments/{sample_comment_id}', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_comment_id}, {'$set': sample_comment})
    
if __name__ == '__main__':
    unittest_main()