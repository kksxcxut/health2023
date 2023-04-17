from PyQt5.QtCore import Qt, QTimer, QTime

def timer_test(self):
  global time 
  time = QTime(0, 0, 15)
  self.timer = QTimer
  self.timer.timeout.connect(self.timer1Event)
  self.timer.start(1000)
  
def timer_test(self):
  global time 
  time = QTime(0, 0, 30)
  self.timer = QTimer()
  self.timer.timeout.connect(self.timer2Event)
  self.timer.start(1500)
  
def timer_test(self):
  global time 
  time = QTime(0, 1, 0)
  self.timer = QTimer
  self.timer.timeout.connect(self.timer1Event)
  self.timer.start(1000)
  
def timer1Event(self):
  global time 
  time = timeaddsecs(-1)
  self.text_timer.setText(time.toString('hh:mm:ss'))
  self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
  self.text_timersetStyleSheet('color: rgb(0, 0, 0)')
  if time.toString('hh:mm:ss') == "00:00:00":
    self.timer.stop()
                               
def timer2Event(self):
  global time 
  time = timeaddsecs(-1)
  self.text_timer.setText(time.toString('hh:mm:ss'))
  self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
  self.text_timersetStyleSheet('color: rgb(0, 0, 0)')
   if time.toString('hh:mm:ss') == "00:00:00":
    self.timer.stop()
   
def timer3Event(self):
  global time 
  time = timeaddsecs(-1)
  self.text_timer.setText(time.toString('hh:mm:ss'))
  if int(time.toString('hh:mm:ss')[6:8] >= 45:
     self.text_timer.setStyleSheet('color: rgb(0,255, 0)')
  elif int (time.toString('hh:mm:ss')[6:8]) <= 15:
    self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
  else:
     self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
    self.text_timersetStyleSheet('color: rgb(0, 0, 0)')
    if time.toString('hh:mm:ss') == "00:00:00":
      self.timer.stop()
    
 def connects(self):
  self.btn_next.cliked.connect(self.next_click)
  self.btn_test1.cliked.connect(self.timer_test)
  self.btn_test3.cliked.connect(self.timer_final) 

      
