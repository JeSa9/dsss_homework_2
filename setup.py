from setuptools import setup

setup(
   name='math_quiz',
   version='1.0.0',
   description='This packages contains a math quiz with some math questions',
   author='Jessica Sarris',
   author_email='Jessie.Sarris@gmx.de',
   packages=[math_quiz/math_quiz],
   install_requires=[
      "unittest",
      "random",
   ],
   scripts=["math_quiz.py", "tests_math_quiz.py"],  
)