import os
import subprocess
import pytest


def cd1(cmd):
    a = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return a.stdout


def output(test_input):
    output1 = cd1(test_input)
    return output1


def check_list(cmd):
    list1 = []
    for i in cmd:
        if i in list1:
            list1.append()
    r = False not in list1
    return r


@pytest.mark.parametrize("test_input", ['cd', 'cd -L', 'cd -P', 'cd -e'])
def test_cd1(test_input):
    p = output(test_input)
    assert check_list(p)


@pytest.mark.parametrize("test_input", ['cd /home/softnautics/Downloads'])
def test_cd2(test_input):
    path = '/home/softnautics/Downloads'

    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False


@pytest.mark.parametrize("test_input", ['cd ../ /home/softnautics/Downloads/textdemo'])
def test_cd3(test_input):
    path = '/home/softnautics/Downloads/textdemo'
    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False


@pytest.mark.parametrize("test_input", ['cd -@ /home/softnautics/Desktop'])
def test_cd4(test_input):
    path = '/home/softnautics/Desktop'

    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False


@pytest.mark.parametrize("test_input",
                         ['cd -- /home/softnautics/Desktop/demo.robot'])  # Wrong directory - assertionerror occured
def test_cd5(test_input):
    path = '/home/softnautics/Desktop/demo.robot'

    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False


@pytest.mark.parametrize("test_input", ['cd - /home/softnautics/Documents'])  # change previous dir
def test_cd6(test_input):
    path = '/home/softnautics/Documents'

    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False


@pytest.mark.parametrize("test_input", ['cd . /home/softnautics/Downloads'])  # Change working directory to current working directory
def test_cd6(test_input):
    path = '/home/softnautics/Downloads'

    if os.path.isdir(path):
        output(test_input)
        assert True
    else:
        assert False

#******************************************************************************************************************************

@pytest.mark.parametrize("test_input", ['cd /','cd ~','cd -','cd --','cd ../','cd ../../'])
def test_cd01(test_input):
    result = output(test_input)
    assert check_list(result)

@pytest.mark.parametrize("test_input", ['cd /home/softnautics/Documents/Sample'])
def test_cd02(test_input):
    path = '/home/softnautics/Documents/Sample'
    if os.path.isdir(path) :
         output(test_input)
         assert True
    else:
         assert False

# cd " "- used to navigate to a directory with white spaces, cd dir\ name - same as cd " "
@pytest.mark.parametrize("test_input", ['cd "/home/softnautics/Documents/UnitTest Framework"'])
def test_cd03(test_input):
    path = '/home/softnautics/Documents/UnitTest Framework'
    if os.path.isdir(path) :
         output(test_input)
         assert True
    else:
         assert False

@pytest.mark.parametrize("test_input", ['cd /home/softnautics/Downloads && ls'])
def test_cd04(test_input):
    path = '/home/softnautics/Downloads'
    if os.path.isdir(path) :
         output(test_input)
         assert True
    else:
         assert False

@pytest.mark.parametrize("test_input", ['cd ~/home/softnautics'])
def test_cd05(test_input):
    path = '/home/softnautics'
    if os.path.isdir(path) :
         output(test_input)
         assert True
    else:
         assert False


