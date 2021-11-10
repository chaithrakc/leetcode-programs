class SolutionReformatDate:
    def reformat_date(self, date: str) -> str:
        month_mapping = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05',
                         'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
                         'Nov': '11', 'Dec': '12'}
        date_list = date.split(' ')
        print(date_list[0][:-2])
        extracted_day = '0' + date_list[0][:-2] if len(date_list[0]) == 3 else date_list[0][:-2]
        extracted_month = month_mapping[date_list[1]]
        extracted_year = date_list[2]
        return f'{extracted_year}-{extracted_month}-{extracted_day}'
