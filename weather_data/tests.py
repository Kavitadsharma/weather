from django.test import TestCase

# Create your tests here.
class WeatherViewTest(TestCase):

    # ... Existing test methods ...

    def test_create_weather(self):
        data = {'city': 'Chicago', 'temperature': 15, 'weather': 'Cloudy'}
        response = self.client.post(reverse('create_weather'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get(reverse('weather', kwargs={'city': 'Chicago'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 15, 'weather': 'Cloudy'})

    def test_update_weather(self):
        data = {'temperature': 25}
        response = self.client.put(reverse('update_weather', kwargs={'city': 'San Francisco'}), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 204)

        response = self.client.get(reverse('weather', kwargs={'city': 'San Francisco'}))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'temperature': 25, 'weather': 'Cloudy'})

    def test_delete_weather(self):
        response = self.client.delete(reverse('delete_weather', kwargs={'city': 'Austin'}))
        self.assertEqual(response.status_code, 204)

        response = self.client.get(reverse('weather', kwargs={'city': 'Austin'}))
        self.assertEqual(response.status_code, 404)
