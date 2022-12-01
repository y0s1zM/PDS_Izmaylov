use pds;
select avg(salary) as СередняЗП, count(distinct employee_id) as Кількістьпрацівників  from employees;