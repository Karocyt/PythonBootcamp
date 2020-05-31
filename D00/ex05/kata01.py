#! /usr/bin/env python3

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    print("\n".join(
        f"{lang} was created by {languages[lang]}" for lang in languages))
