git-example:
	ansible-playbook -i "localhost," echo_git_revision.yml -c local

test_tty:
	python3 -c "import sys; print(sys.stdout.isatty())"
