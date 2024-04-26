import pytest

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        }
    ]
    

def format_data_for_display(people_data):
    return [f"{person['given_name']} {person['family_name']}: {person['title']}" for person in people_data]

def format_data_for_excel(people_data):
    data = "given,family,title\n"
    family = ''.join([f"{person['given_name']},{person['family_name']},{person['title']}\n" for person in people_data])
    return data + family


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    expected_output = """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
    assert format_data_for_excel(example_people_data) == expected_output

