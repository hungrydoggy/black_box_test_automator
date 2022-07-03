import subprocess



def main ():
  _runTestUnit('/home/john/Projects/SikuliProjects/test.sikuli')


def _runTestUnit (filepath):
  print(f'java -jar sikulixide-2.0.5-lux.jar -r {filepath}')
  pr = subprocess.run(
      ['java', '-jar', '/home/john/Apps/Sikuli/sikulixide-2.0.5-lux.jar', '-r', filepath],
      stdout=subprocess.PIPE,
      text=True
  )


  # switch-case for pr.returncode
  (
    {
      0: _runTestUnit_caseSuccess,
      1: _runTestUnit_caseFailed,
    }[pr.returncode] or _runTestUnit_caseDefault
  )(pr)

def _runTestUnit_caseSuccess (pr):
  _printSubprocessResult(pr)

def _runTestUnit_caseFailed (pr):
  _printSubprocessResult(pr)

def _runTestUnit_caseDefault (pr):
  _printSubprocessResult(pr)

def _printSubprocessResult (pr):
  print('#'*5, 'returncode')
  print(pr.returncode)
  print('#'*5, 'stdout')
  print(pr.stdout)
  print('#'*5, 'stderr')
  print(pr.stderr)



main()
