import contextlib

# class just_some_exceptions:
#     def __init__(self):
#         self.dictionary = {'Name': 'Gabi', 'AGE':29}
# #
#     def __enter__(self):
#         return self.dictionary
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         try:
#             dict_age = dict['AGE']
#             print(dict_age)
#             dict_height = dict['Height']
#             print(dict_height)
#         except KeyError as ke:
#             print('Key Not in dictionary:', ke)
#         finally:
#             return
#
# with just_some_exceptions() as dict:
#     print('*' * 70)
#     print(dict)

#
#
# class just_some_exceptions:
#     def __init__(self):
#         self.list = [1, 2, 3, 4, 5, 6, 7]
#
#     def __enter__(self):
#         return self.list
#
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         error_message = ''
#         try:
#             print(list[5])
#         except IndexError as e:
#             print(e)
#             error_message = 'The number is out of range'
#         finally:
#             if error_message:
#                 print(error_message)
#             else:
#                 print('Number accepted')
#
# with just_some_exceptions() as list:
#     print('Some list')
#     print(list)

# @contextlib.contextmanager
# def just_some_exceptions():
#     dict = {'Name': 'Gabi', 'AGE': 29}
#
#     yield
#     error_message = ''
#     try:
#         dict_age = dict['AGE']
#         dict_height = dict['Height']
#         print(dict_age)
#         print(dict_height)
#
#     except KeyError as ke:
#         error_message = 'The key is not found'
#     finally:
#         if error_message:
#             print(error_message)
#
# with just_some_exceptions() as dict:
#     print('-'* 77)


# @contextlib.contextmanager
# def just_some_exceptions():
#     list = [1, 2, 3, 4, 5, 6, 7]
#     yield
#     print(list)
#     error_message = ''
#     try:
#         print(list[5])
#
#     except IndexError as e:
#         print(e)
#         error_message = 'Please try again'
#     finally:
#         if error_message:
#             print(error_message)
#         else:
#             print('Number accepted')
#
# with just_some_exceptions() as list:
#     print()
















