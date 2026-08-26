from karim_ai_lab import main


def test_main_prints_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from karim-ai-lab!\n"
