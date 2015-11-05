#!/usr/bin/env python
"""Takes the output of task <report> and prints it on the desktop using Ubersicht."""

import sys
import subprocess

def tasksync():
    """Sync Taskwarrior with In the AM"""
    bashCommand = "/usr/local/bin/task sync 2>/dev/null"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output - process.communicate()[0]
    
def taskreport():
    """Pull Taskwarrior report"""
    bashCommand = "/usr/local/bin/task desktop 2>/dev/null"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output - process.communicate()[0]

def parse():
    """This is the function"""

    taskarray = []
   
    for line in sys.stdin:
        taskarray.append(line) # = tasklist + line

    if not taskarray:
      return
    else:

      header = taskarray[2].split()

      row = 0
  #     print '<div class="content-box">'
      print "<h1>Tasks</h1>"
      print "<table>"
      for line in taskarray:
          if len(line) < 10:
              continue

          tag = "<td>"
          tag_end = "</td>"

          if row == 0:
              tag = "<th>"
              tag_end = "</th>"
          pos = 0
          for col in header:
              if row == 1:
                  continue
              if len(line[0:len(header[0])].strip()) == 0:
                  continue
              print tag + line[pos:pos+len(col)].strip() + tag_end
              pos += len(col) + 1
          print "</tr>"
          row += 1
      print "</table>"
  #     print "</div>"

#call main
if __name__ == '__main__':
    parse()
