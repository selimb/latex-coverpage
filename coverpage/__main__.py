import click
from cookiecutter.main import cookiecutter
from functools import partial
import os

from .constants import TEMPLATE_DIR
TEMPLATE_DIR = os.path.expanduser(TEMPLATE_DIR)

COURSES = [
    ('MECH 546', 'Finite Element Methods in Solid Mechanics'),
    ('MECH 539', 'Computational Aerodynamics'),
]

@click.command()
def main():
    print('Pick a course:')
    for i, course in enumerate(COURSES):
        print('%i. %s' % (i, course[1]))
    prompt = partial(click.prompt, '> ', prompt_suffix='')
    chosen_idx = prompt(
        type=click.IntRange(min=0, max=len(COURSES) - 1)
    )
    print('Title:')
    title = prompt()
    chosen_course = COURSES[chosen_idx]
    course_code = chosen_course[0]
    course_name = chosen_course[1]
    repo_name = 'tex'
    print('Using template at: %s' % TEMPLATE_DIR)

    cookiecutter(
        TEMPLATE_DIR,
        no_input=True,
        extra_context={
            'repo_name': repo_name,
            'title': title,
            'course_code': course_code,
            'course_name': course_name,
        }
    )

if __name__ == '__main__':
    main()
