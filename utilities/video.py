from .webcamstream import WebcamStream

class VideoStream:
	def __init__(self, src=0):

		self.stream = WebcamVideoStream(src=src)

	def start(self):

		return self.stream.start()

	def update(self):

		self.stream.update()

	def read(self):

		return self.stream.read()

	def stop(self):

                self.stream.stop()
