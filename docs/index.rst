========================
django-zinibu-skeleton
========================

Documentation for skeleton Django application used by the zinibu project.

-------------------
Using pip
-------------------

You should first switch to the virtual environment you will be using with pyvenv or virtualenv.

To install from the source using a version control system, git in this case, use --editable (-e):
  ``pip install -e git://github.com/user/django-zinibu-skeleton#egg=django-zinibu-skeleton``

Use django-zinibu-skeleton, what was defined with the #egg parameter, for uninstalling:
  ``pip uninstall django-zinibu-skeleton``

You can also install from the source path, which helps while developing the application while keeping it installed:
  ``pip install -e /home/user/django-zinibu-skeleton``

--editable is actually optional so you can:
  ``pip install /home/user/django-zinibu-skeleton``

You can see what version of the module you're using and the path where it's coming from by going to the Python shell and running:
  ``import znbskeleton``
  ``print znbskeleton.VERSION``
  ``print znbskeleton.__file__``

You can see what packages are installed at any moment:
  ``pip freeze``

And you can uninstall the same way you did when using a source from version control:
  ``pip uninstall django-zinibu-skeleton``

Underscores should work too:

  ``pip uninstall django_zinibu_skeleton``

-----------------------------
More information about  pip
-----------------------------

https://packaging.python.org/en/latest/installing/
