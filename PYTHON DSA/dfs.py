# # Given a grap containing managers and their employees as a dictionary of  sets, print  all  employees reporting to a  given manager.
# # data = {
# #     "karan": {"darshan", "nikhil"},
# #     "darshan": {"khantil", "tanuj"},
# #     "tanuj": {"nikhil"},
# #     "krinish": {"hetul"},
# #     "khantil": set(),
# #     "nikhil": set()
# # }
#
# # Example: Darshan and Nikhil are reporting to
# # Karan.Khantil and Tanuj  are reporting to Darshan.
# #
# # Q.Find all employees who are reporting to Karan.
# # Explanation:
#
# # -So here, we want to find all the children nodes of Karan.
#
# # -We will perform DFS
# # starting on
# # Karan and then traverse all the children of
# # Karan which are unvisited.
# # Output:
# # karan: nikhil darshan tanuj khantil
#
# def find_employees(data, start, employee, visited=set()):
#     # if not visited print it
#     if start not in visited:
#         print(start, end=" ")
#         if start == employee:
#             print(":", end=" ")
#     visited.add(start)
#
#     for i in data[start] - visited:
#         # if not visited go in depth of it
#         find_employees(data, i, visited)
#     return
#
#
# # sample data in dictionary form
# data = {
#     "karan": {"darshan", "nikhil"},
#     "darshan": {"khantil", "tanuj"},
#     "tanuj": {"nikhil"},
#     "krinish": {"hetul"},
#     "khantil": set(),
#     "nikhil": set()
# }
#
#
# if __name__ == '__main__':
#
#     find_employees(data, "karan", "karan")