# import user_define_module
#
# print(user_define_module.sum(2, 3))
# print(user_define_module.mult(9, 0))

# # call(): for specific function
#
# from user_define_module import sum
# print(sum(1, 2))
# print(mult(1, 2)) /// Error

# # for all functions
#
# from user_define_module import*
# print(mult(2, 3))
# print(sum(2, 3))

# #  the import........ as statement : renaming
#
# import user_define_module as mod
# print(mod.mult(2, 3))

# # multiple modules :
#
# import user_define_module, user_define_module2
# print(user_define_module2.sub(2, 4))
# print(user_define_module.mult(2, 2))

