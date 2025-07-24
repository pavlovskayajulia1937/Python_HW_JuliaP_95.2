from ProjectApi import ProjectApi
from config import ADMIN, WORKER


def test_create_project():
    title = "Учеба"
    project_api = ProjectApi()
    result = project_api.create_project(title, WORKER)
    new_id = result["id"]

    assert new_id is not None


def test_edit():
    new_title = "Учеба2"
    project_api = ProjectApi()
    result = project_api.create_project("Учеба", WORKER)
    new_id = result["id"]

    new_project = project_api.edit(new_title, new_id)

    assert new_project.status_code == 200


def test_get_project():
    project_api = ProjectApi()
    result = project_api.create_project("Учеба", WORKER)
    new_id = result["id"]

    new_project = project_api.get_project(new_id)

    assert new_project["id"] == new_id


# Тест неудачного создания проекта (например, пустое название)
def test_project_negative():
    title = ""
    project_api = ProjectApi()
    result = project_api.create_project(title, {})
    assert result["message"] == ['title should not be empty']


# Тест попытки получить проект с неверным id
def test_id_project_negative():
    project_api = ProjectApi()
    result = project_api.get_project("87486856856")

    assert result["message"] == 'Проект не найден'
