import pusher

pusher_client = pusher.Pusher(
  app_id='1711276',
  key='107f169fb90c869fb329',
  secret='480882bb53caf644843b',
  cluster='ap2',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})