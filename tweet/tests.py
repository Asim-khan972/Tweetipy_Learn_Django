from django.test import TestCase
from django.contrib.auth.models import User
from .models import Tweet

# Create your tests here.

class TweetModelTest(TestCase):
    def test_str(self):
        tweet = Tweet.objects.create(
            user = User.objects.create_user(username='testuser'),
            text = 'test tweet',
        )
        self.assertEqual(str(tweet), 'testuser - test tweet')   

    def test_get_absolute_url(self):
        tweet = Tweet.objects.create(
            user = User.objects.create_user(username='testuser'),
            text = 'test tweet',
        )
        self.assertEqual(tweet.get_absolute_url(), '/tweet_list/')

    def test_tweet_list_view(self):
        response = self.client.get('/tweet_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tweet_list.html')
        self.assertContains(response, 'No tweets found.')

    def test_tweet_create_view(self):
        response = self.client.get('/tweet_create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tweet_form.html')

    def test_tweet_update_view(self):
        tweet = Tweet.objects.create(
            user = User.objects.create_user(username='testuser'),
            text = 'test tweet',
        )
        response = self.client.get(f'/tweet_update/{tweet.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tweet_form.html')

    def test_tweet_delete_view(self):
        tweet = Tweet.objects.create(
            user = User.objects.create_user(username='testuser'),
            text = 'test tweet',
        )
        response = self.client.get(f'/tweet_delete/{tweet.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tweet_confirm_delete.html')

    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')    

    def test_logout_view(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logout.html')    

    def test_profile_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')
        self.assertContains(response, 'No tweets found.')   

    def test_password_change_view(self):
        response = self.client.get('/password_change/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_change.html')
        self.assertContains(response, 'Change Password')

    def test_password_change_done_view(self):
        response = self.client.get('/password_change/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_change_done.html')
        self.assertContains(response, 'Your password has been changed successfully.')

    def test_password_reset_view(self):
        response = self.client.get('/password_reset/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset.html')
        self.assertContains(response, 'Reset Password')

    def test_password_reset_done_view(self):
        response = self.client.get('/password_reset/done/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_done.html')
        self.assertContains(response, 'Check your email for instructions.')

    def test_password_reset_confirm_view(self):
        response = self.client.get('/password_reset/confirm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')
        self.assertContains(response, 'Enter new password')

    def test_password_reset_complete_view(self):
        response = self.client.get('/password_reset/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')
        self.assertContains(response, 'Your password has been reset successfully.')

    def test_password_reset_confirm_view(self):
        response = self.client.get('/password_reset/confirm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')
        self.assertContains(response, 'Enter new password')

    def test_password_reset_complete_view(self):
        response = self.client.get('/password_reset/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')
        self.assertContains(response, 'Your password has been reset successfully.')

    def test_password_reset_confirm_view(self):
        response = self.client.get('/password_reset/confirm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')
        self.assertContains(response, 'Enter new password')

    def test_password_reset_complete_view(self):
        response = self.client.get('/password_reset/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')
        self.assertContains(response, 'Your password has been reset successfully.')

    def test_password_reset_confirm_view(self):
        response = self.client.get('/password_reset/confirm/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_confirm.html')
        self.assertContains(response, 'Enter new password')

    def test_password_reset_complete_view(self):
        response = self.client.get('/password_reset/complete/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_complete.html')
        self.assertContains(response, 'Your password has been reset successfully.')

    