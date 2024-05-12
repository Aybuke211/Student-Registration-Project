# Student-Registration-Project
Student-Course Registration System by using Python Tkinter and Mysql

MySQL Codes:
CREATE DATABASE student_course;
USE student_course;
CREATE TABLE Students(student_id  INT auto_increment primary KEY,
					  first_name VARCHAR(50),
                      last_name VARCHAR(50),
                      birth_date DATE,
                      gender ENUM('MALE' , 'FEMALE'),
                      class INT); 
                      
CREATE TABLE Courses(
					course_id INT auto_increment primary key,
					course_name VARCHAR(50),
					instructor VARCHAR(50),
					hours INT);
		
CREATE TABLE student_courses (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
