from threading import Thread
import sys
import cv2
import time

if sys.version_info >= (3, 0):
	from queue import Queue

else:
	from Queue import Queue

class FileVideoStream:
	def __init__(self, path, transform=None, queueSize=128):
		self.stream = cv2.VideoCapture(path)
		self.stopped = False
		self.transform = transform
		self.Q = Queue(maxsize=queueSize)

	def start(self):
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return

			if not self.Q.full():
				(grabbed, frame) = self.stream.read()
				if not grabbed:
					self.stop()
					return

				if self.transform:
					frame = self.transform(frame)

				self.Q.put(frame)
			else:
				time.sleep(0.1)  # Rest for 10ms, we have a full queue  

	def read(self):
		return self.Q.get()

	def running(self):
		return self.more() or not self.stopped

	def more(self):
		return self.Q.qsize() > 0

	def stop(self):
                self.stopped = True
