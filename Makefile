git-example:
	ansible-playbook -i "localhost," echo_git_revision.yml -c local

test_tty:
	python3 -c "import sys; print(sys.stdout.isatty())"

clean:
	find . -type f -regex ".*\py[co]$$" -delete
	find . -type d -name "__pycache__" -delete
