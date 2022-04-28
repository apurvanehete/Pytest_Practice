import pytest
import subprocess
import os


def cp_1(cmd):
    p = subprocess.run(cmd, shell=True, encoding='utf-8', stdout=subprocess.PIPE)
    return p.stdout


def result(command):
    output = cp_1(command)
    return output


@pytest.mark.parametrize("command", ['cp', 'cp -version', 'cp text1.txt text2.txt','cp -f text1.txt text2.txt','cp -l text1.txt text4.txt','cp -s text1.txt text5.txt'])
def test_cp1(command):
    result(command)
    assert True


@pytest.mark.parametrize("command", ['cp -r text3.txt /home/softnautics/Downloads'])
def test_cp2(command):
    result(command)
    path = '/home/softnautics/Downloads'
    isExist = os.path.exists(path)
    assert isExist


@pytest.mark.parametrize("command", ['cp /home/softnautics/Documents/text3.txt /Download'])
def test_cp3(command):
    path = '/Download'
    if os.path.exists(path):
        result(command)
        assert True
    else:
        assert False

@pytest.mark.parametrize("command",['cp  -r text1.txt text2.txt /home/softnautics/Downloads '])
def test_cp4(command):
   path = '/home/softnautics/Downloads'
   if  os.path.exists(path) :
    result(command)
    assert True
   else :
    assert False

# -b(backup),-p(preserve-the time of the last data modification and the time)
@pytest.mark.parametrize("command", ['cp -i text1.txt text2.txt',' cp -b text1.txt text2.txt','cp -p text1.txt text2.txt'])
def test_cp5(command):
    result(command)
    assert True

@pytest.mark.parametrize("command", ['cp -v /home/softnautics/Documents/text3.txt /home/softnautics/Downloads','cp -iv text2.txt /home/softnautics/Downloads'])
def test_cp6(command):
    path_dir = '/home/softnautics/Downloads'
    if os.path.exists(path_dir):
        result(command)
        assert True
    else:
        assert False

#Copying using * wildcard
@pytest.mark.parametrize("command", ['cp *.txt Folder1'])
def test_cp7(command):
    path_dir = 'Folder1'
    if os.path.exists(path_dir):
        result(command)
        assert True
    else:
        assert False

@pytest.mark.parametrize("command", ['cp -a /home/softnautics/Documents/text3.txt /home/softnautics/Downloads','cp -n text1.txt /home/softnautics/Downloads'])
def test_cp8(command):
    path_dir = '/home/softnautics/Downloads'
    if os.path.exists(path_dir):
        result(command)
        assert True
    else:
        assert False

@pytest.mark.parametrize("command", ['cp -u file_*.txt /home/softnautics/Downloads'])
def test_cp9(command):
    path_dir = '/home/softnautics/Downloads'
    if os.path.exists(path_dir):
        result(command)
        assert True
    else:
        assert False








