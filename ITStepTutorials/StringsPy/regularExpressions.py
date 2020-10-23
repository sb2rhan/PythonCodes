import re # getting regEx module

# All of these methods return Match object

# # works as str.startswith()
# m_result = re.match('Lorem', 'Lorem ipsum')
# print(m_result.group()) # string

# # works as str.contains() only first occurrence
# s_result = re.search('ip', 'Lorem ipsum')
# print(s_result)

# # every occurrences
# f_result = re.findall('ip', 'Lor oip ip er ip')
# print(f_result) # list


# spl_result = re.split('s', 'Jason sock moson')
# print(spl_result)


# sub_result = re.sub('\t', ' ', 'Some i\t tech companies\t IT')
# print(sub_result)

# # prepares template for using it
# c_template = re.compile('\t')
# c_result = c_template.split('Hello\tfriend!')
# print(c_result)


#       Using regEx
# pattern = re.compile(r'[A-Z]+')
# result = pattern.findall('Hello World! MY name is ...')
# print(result)


# searching domen names
# emails = 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz'
# pattern = re.compile(r'\@\w+\.\w+')
# domens = pattern.findall(emails)

# for domen in domens:
#     print(domen[1:])


# searching dates
# text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
# pattern = re.compile(r'\d{2}\-\d{2}\-\d{4}')
# dates = pattern.findall(text)
# print(dates)
