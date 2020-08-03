# ！/usr/bin/env/ python
# coding=utf-8
from apis.contract.department.depmanagment import DeptManagment


class TestCreateDep:
    def test_create_new_dep(self):
        dept_management = DeptManagment()
        dept_management.create_dept()
        create_res = dept_management.get_response()
        assert create_res.get('errmsg') == 'created'
