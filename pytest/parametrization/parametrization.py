import pytest



def is_palindrome(maybe_palindrome:str) -> bool:
    reprocessed_palindrome =  maybe_palindrome.lower().replace(" ","")
    return reprocessed_palindrome == reprocessed_palindrome[::-1]

@pytest.mark.parametrize("maybe_palindrome, expected_result",[
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God", True),
    ("abc", False),
    ("abab", False),
])
def test_is_a_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result    