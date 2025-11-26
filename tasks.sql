USE company_db;
select * from employees;

-- 1. Find the youngest emp in the company
SELECT * FROM employees
ORDER BY age ASC
LIMIT 1;

SELECT * FROM employees
WHERE age = (SELECT MIN(age) FROM employees);

-- 2. Count how many employees are in each department.
SELECT * FROM departments;
SELECT d.dept_name, COUNT(*) AS total_employees
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_employees DESC;

-- Show only female employees with salary above ₹45,000.
SELECT * FROM employees
WHERE gender = 'F' AND salary > 45000;


-- 3. Show employee name, department name, and location.

SELECT e.name AS Employee_Name,
d.dept_name AS Department_Name,
d.location AS Location
FROM employees e
INNER JOIN departments d 
ON e.dept_id = d.dept_id;

-- 4. Show each employee’s salary and how much higher it is than the company average.

SELECT AVG(salary) FROM employees;

SELECT name AS Employee_Name,
salary AS Salary,
salary - (SELECT ROUND(AVG(salary),2) FROM employees) AS Higher_Than_Avg
FROM employees
WHERE salary > (SELECT ROUND(AVG(salary), 2) FROM employees);

-- 5. Show each employee’s salary and how much higher it is than the company average including dept name and locations

SELECT 
    e.name AS Employee_Name,
    e.salary AS Salary,
    e.salary - (SELECT ROUND(AVG(salary),2) FROM employees) AS Higher_Than_Avg,
    d.dept_name AS Department_Name,
    d.location AS Location
FROM employees e
INNER JOIN departments d 
ON e.dept_id = d.dept_id
WHERE e.salary > (SELECT AVG(salary) FROM employees);

-- 6. Show running total of salary within each department.

SELECT e.name, d.dept_name, e.salary,
		SUM(e.salary) OVER (PARTITION BY d.dept_name ORDER BY e.salary) AS running_total
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 7. Display previous and next employee salary compared to each employee.

SELECT e.name,e.salary,
    LAG(e.salary) OVER (ORDER BY e.salary) AS previous_salary, -- it takes previous one
    LEAD(e.salary) OVER (ORDER BY e.salary) AS next_salary -- it takes next one
FROM employees e;

-- 8. Display previous and next employee salary compared to each employee within each dept

SELECT e.name, d.dept_name, e.salary,
    LAG(e.salary) OVER (PARTITION BY d.dept_name ORDER BY e.salary) AS previous_salary,
    LEAD(e.salary) OVER (PARTITION BY d.dept_name ORDER BY e.salary) AS next_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- 9. Find the top 3 highest-paid employees in each department.

-- its in sub query bcoz some sql engine wont allow windows function in the where clause
-- ranked- -- every derived table must have it own alias 

INSERT INTO employees
VALUES (114, 'Advika', 23, 'F', 2, '2024-10-24', 35000);

SELECT name, dept_name, salary, salary_rank
FROM (
    SELECT e.name, d.dept_name, e.salary,
        DENSE_RANK() OVER ( PARTITION BY d.dept_name ORDER BY e.salary DESC) AS salary_rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
) AS ranked 
WHERE salary_rank <= 3;

-- SELECT e.name, d.dept_name, e.salary,
--    DENSE_RANK() OVER ( PARTITION BY d.dept_name ORDER BY e.salary DESC) AS salary_rank
-- FROM employees e
-- JOIN departments d ON e.dept_id = d.dept_id
-- WHERE DENSE_RANK() OVER (PARTITION BY d.dept_name ORDER BY e.salary DESC) <= 3; -- some sql engine wont allow windows function in the where clause

-- 10. Find employees earning more than twice their department average salary.

INSERT INTO employees
VALUES (119, 'Kavya', 26, 'F', 2, '2015-10-20', 300000);

INSERT INTO employees
VALUES (118, 'Katie', 32, 'F', 5, '2015-11-20', 250000);

SELECT name, dept_name, salary, dept_avg_salary
FROM (
    SELECT e.name, d.dept_name, e.salary,
        AVG(e.salary) OVER (PARTITION BY d.dept_name) AS dept_avg_salary
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
) AS sub
WHERE salary > 2 * dept_avg_salary;

-- Another method without window funtion

SELECT e.name, d.dept_name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 2 * (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e.dept_id
);
-- 11. Calculate 3-row moving average of salaries.

-- Moving Average= Sum of included salaries​ / Number of included rows 
-- According to formula Dinesh = (35000)/1 = 35000 bcoz there is no previous row, Advika = (35000+35000)/2 = 35000, Anjali = (35000 + 35000 + 38000)/3 = 36000
-- only 3 rows it will take
-- window function AVG - window function calculates the average for each row
-- OVER - turns it into a window function (no grouping)
-- ROWS BETWEEN 2 PRECEDING AND CURRENT ROW - to average the current row + 2 previous rows that is 3 row
-- if emp_id = 2 , the query looks at emp_id BETWEEN 0 and 2 , but no employee in emp_id = 0
 
SELECT e.name, e.salary,
    AVG(e.salary) OVER ( 
		ORDER BY e.salary
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_salary
FROM employees e;

-- without windows function
-- BETWEEN e1.employee_id - 2 AND e1.employee_id - look at the current row and previous 2 rows based on order

SELECT e1.employee_id, e1.name, e1.salary,
    (
        SELECT AVG(e2.salary)
        FROM employees e2
        WHERE e2.employee_id BETWEEN e1.employee_id - 2 AND e1.employee_id
    ) AS moving_avg_salary
FROM employees e1
ORDER BY e1.employee_id;

-- 12. Simulate month-over-month salary growth using LAG()

-- Create table
CREATE TABLE employee_salaries (
    employee_id INT,
    name VARCHAR(50),
    salary_month DATE,
    salary DECIMAL(10,2)
);
-- Insert employees
INSERT INTO employee_salaries (employee_id, name, salary_month, salary) VALUES
(1, 'Arjun', '2025-01-01', 3000),
(1, 'Arjun', '2025-02-01', 3200),
(1, 'Arjun', '2025-03-01', 3400),
(1, 'Arjun', '2025-04-01', 3500),
(2, 'Kavya', '2025-01-01', 2800),
(2, 'Kavya', '2025-02-01', 2900),
(2, 'Kavya', '2025-03-01', 3000),
(2, 'Kavya', '2025-04-01', 3100),
(3, 'Priya', '2025-01-01', 5000),
(3, 'Priya', '2025-02-01', 5100),
(3, 'Priya', '2025-03-01', 5200),
(3, 'Priya', '2025-04-01', 5300);

-- salary - current salary
-- LAG(salary) - previous salary
-- growth_pct(%) = ((current salary - previous salary) / previous salary) ​×100

SELECT employee_id, name, salary_month, salary,
    LAG(salary) OVER (
        PARTITION BY employee_id
        ORDER BY salary_month
    ) AS prev_month_salary,
    salary - LAG(salary) OVER (
        PARTITION BY employee_id
        ORDER BY salary_month
    ) AS salary_growth,
    ROUND(
        ((salary - LAG(salary) OVER (PARTITION BY employee_id ORDER BY salary_month)) 
        / LAG(salary) OVER (PARTITION BY employee_id ORDER BY salary_month)) * 100, 2
    ) AS growth_pct
FROM employee_salaries
ORDER BY employee_id, salary_month;









