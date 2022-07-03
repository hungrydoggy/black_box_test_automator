import os
import shutil
import time

from sikuli.Sikuli import *



g_judge_res_list_ = []  # JudgeResult[]


def test (func, params=[]):
  global g_judge_res_list_

  # ready
  g_judge_res_list_ = []

  callee_path = _findCalleePath()
  print(callee_path)


  # run test unit
  try:
    func(*params)
  except FindFailed as e:
    print('!@#@!'),
    print(e)
    raise e

  
  ## process with results of judges
  if len(g_judge_res_list_) <= 0:
    raise Exception('no judged')
  
  # write detail report to GS
  for jr in g_judge_res_list_:
    # TODO
    pass

  # write brief to GS
  if _isAllSuccess(g_judge_res_list_) == True:
    # TODO
    pass
  else:
    # TODO
    pass


def judge (region, img_path, similarity, wait_time):
  global g_judge_res_list_

  pattern = Pattern(img_path).similar(similarity)
  m = region.exists(pattern, wait_time)

  jr = JudgeResult(m != None, region, img_path, similarity, m)
  g_judge_res_list_.append(jr)
  return jr




class JudgeResult:
  def __init__ (self, is_success, region, what_we_need, similarity, match):
    self.is_success   = is_success
    self.region       = region
    self.what_we_need = what_we_need
    self.similarity   = similarity
    self.match        = match

    screen = region.getScreen()
    self.captured_path = screen.capture(region).save('tmp')

    if is_success == True:
      # TODO draw rectangle on match
      pass



def _findCalleePath ():
  for fp in map(lambda e: e[1], inspect.stack()):
    if fp.find('.sikuli') >= 0:
      return fp

  raise Exception('cannot find ".sikuli" on path')

def _isAllSuccess (judge_results):
  for jr in judge_results:
    if jr.is_success == False:
      return False

  return True
