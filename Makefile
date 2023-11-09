test-sender:
	pytest sender_test.py -v

test-receiver:
	pytest receiver_test.py -v

test-all: test-sender test-receiver