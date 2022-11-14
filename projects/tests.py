from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="Test Project 1")
        Project.objects.create(title="Test Project 2")
    
    def test_projects_exist(self):
        project1 = Project.objects.get(title="Test Project 1")
        self.assertTrue(project1.title, "Test Project 1")

        project2 = Project.objects.get(title="Test Project 2")
        self.assertTrue(project2.title, "Test Project 2")
    
    def test_project_doesnt_exist(self):
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(title="Test Project 3")
    
    def test_multiple_projects_get_error(self):
        with self.assertRaises(Project.MultipleObjectsReturned):
            Project.objects.get(title__startswith="Test Project")