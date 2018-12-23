from deal_all_infor.scanf_all import scanTask
# from tests import tests
if  __name__  ==  "__main__":
    """
    测试
    """
    test_func = scanTask('10.10.9.1-10.10.9.255', 3305, 3307, ["mysql"])
    # test_func.scanf_part()
    test_func.run()