import random
import os
import json
TaskPath = '/Users/payalingale01/Projects/PythonProjects/todolist/taskList.json'


def loadData ():
  if(os.path.exists(TaskPath)):
    with open(TaskPath,'r') as f:
      return json.load(f)
  return {}


def userInput(taskData):
  taskName = input('Enter Task Name:- ')
  priority = input('Priority (high/medium/low):- ')
  date = input('Due date (YYYY-MM-DD):- ')
  id = str(random.randint(1,100))

  while taskName == '':
    print('Task Name cannot be empty')
    taskName = input('Enter Task Name:- ')

  while priority == '':
    print('Priority cannot be empty')
    priority = input('Priority (high/medium/low):- ')
  
  while date == '':
    print('Date cannot be empty')
    date = input('Due date (YYYY-MM-DD):- ')

  taskData[id]={
    'taskName':taskName,
    'priority':priority.lower(),
    'status':'pending',
    'date':date
  }
  saveTask(taskData)

  print(f'user input {taskData}')
  return taskData

def saveTask(taskData):
  with open(TaskPath,'w')as f:
    json.dump(taskData,f,indent=1)

def viewAllTask(taskData):
    for index, (task_id, task_info) in enumerate(taskData.items(), start=1):
      print(f"{task_id} : {task_info}")
  
def viewPendingTask(taskData):
  pendingTaskList = []
  for index, (task_id, task_info) in enumerate(taskData.items()):
    if task_info['status'] == 'pending':
      pendingTaskList.append({'id': task_id, 'taskInfo': task_info})
  
  if pendingTaskList:
    print(pendingTaskList)
  else:
    print('No pending task')

  
def markTaskCompleted(taskData):
  id = str(input('Enter the id which needs to mark completed:- '))
  for (task_id, task_info) in taskData.items():
    print(task_id)
    if id in task_id:
      print(f'{task_info}')
      task_info['status'] = 'completed'
      task_info

  saveTask(taskData)  # Save changes to JSON file
  viewAllTask(taskData)

def show_menu():
  print('TO Do List')
  print('1.Add Task')
  print('2.View All Task')
  print('3.View All Pending Task')
  print('4.Mark Task as Completed')
  print('5.Exit')
  

def user_choice(taskData):
  show_menu()
  

def main():
    while True:
      show_menu()
      userChoice = str(input('Select an option:- '))
      taskData = loadData()
      if userChoice == '1':
        userInput(taskData)
      elif userChoice == '2':
        viewAllTask(taskData)
      elif userChoice == '3':
        viewPendingTask(taskData)
      elif userChoice == '4':
        markTaskCompleted(taskData)
      elif userChoice == '5':
        print('GoodBye')
        break
      else:
        print('Invalid choice selected')


main()