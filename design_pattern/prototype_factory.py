# -*- coding: utf-8 -*-
import copy

class Address:
  def __init__(self, street_address, suite, city):
    self.street_address = street_address
    self.suite = suite
    self.city = city

  def __str__(self):
    return f"{self.street_address}, Suite #{self.suite}, {self.city}"


class Employee:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def __str__(self):
    return f"{self.name} works at {self.address}"


class EmployeeFactory:
  # init a placeholder for name and suite with "" & 0
  main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
  aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

  @staticmethod
  def __new_employee(proto, name, suite):
    result = copy.deepcopy(proto)
    result.name = name
    result.address.suite = suite
    return result

  @staticmethod
  def new_main_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee,
                                          name,
                                          suite)

  @staticmethod
  def new_aux_office_employee(name, suite):
    return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee,
                                          name,
                                          suite)


if __name__ == '__main__':
  jane = EmployeeFactory.new_aux_office_employee("Jane", 200)
  print(jane)
