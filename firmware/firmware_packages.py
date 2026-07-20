import lib

@pytest.mark.parameterize("operation",["install","downgrade","update","remove"])
def fw_pkg_test(operation):
    pass