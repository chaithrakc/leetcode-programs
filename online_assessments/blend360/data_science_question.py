import pandas as pd

class FindEmployees:
    def find_next_employee(employee_df:pd.DataFrame):
        school_df = employee_df[employee_df['employer'] == 'School']
        blend360_employees = employee_df[employee_df['employer'] == 'Blend360']
        result_df = pd.merge(school_df, blend360_employees,
                             left_on=['user_id', 'end_date'], right_on=['user_id', 'start_date'],
                             suffixes=('_sh', '_emp'))
        print(result_df[['user_id', 'employer_sh', 'start_date_sh', 'end_date_sh', 'employer_emp', 'start_date_emp']])

if __name__ == '__main__':
    df = pd.DataFrame({
        "user_id":[1,1,2,3,3,4, 5, 5, 4],
        "employer":['School', 'Blend360', 'Blend360', 'School', 'Blend360', 'School', 'School',
                    'Blend360', 'School'],
        "designation":['Student', 'Developer', 'Developer', 'Student', 'Manager', 'Student', 'Student',
                       'Developer', 'Student'],
        "start_date":['16-11-2021','15-05-2023','17-10-2023','15-12-2022','16-07-2024','12-12-2025', '12-12-2021',
                      '12-07-2022', '12-08-2028'],
        "end_date":['15-05-2023', '', '', '16-07-2024', '', '', '12-06-2022',
                    '', '12-09-2028']
    })

    FindEmployees.find_next_employee(df)