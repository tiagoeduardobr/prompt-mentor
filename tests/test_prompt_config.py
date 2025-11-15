import pytest
import yaml
import os

def test_prompt_config_structure():
    """Testa se a estrutura do prompt_config.yaml está correta."""
    with open('mentor/prompt_config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # Verifica se as chaves principais existem
    assert 'llm' in config
    assert isinstance(config['llm'], dict)
    assert 'provider' in config['llm']
    assert 'model' in config['llm']
    assert 'api_key_env' in config['llm']
    assert 'temperature' in config['llm']
    assert 'max_tokens' in config['llm']
    
    # Verifica tipos
    assert isinstance(config['llm']['provider'], str)
    assert isinstance(config['llm']['model'], str)
    assert isinstance(config['llm']['api_key_env'], str)
    assert isinstance(config['llm']['temperature'], (int, float))
    assert isinstance(config['llm']['max_tokens'], int)
    
    # Verifica valores padrão
    assert config['llm']['provider'] == 'openai'
    assert config['llm']['model'] == 'gpt-4-turbo'
    assert config['llm']['api_key_env'] == 'OPENAI_API_KEY'
    assert config['llm']['temperature'] == 0.3
    assert config['llm']['max_tokens'] == 4096
    
    # Verifica outras chaves
    assert 'mentor_guide_file' in config
    assert 'logging_level' in config
    assert 'specializations_dir' in config

def test_env_var_reading():
    """Testa se as variáveis de ambiente são lidas corretamente."""
    # Simula a configuração de uma variável de ambiente
    original_key = os.environ.get('OPENAI_API_KEY')
    os.environ['OPENAI_API_KEY'] = 'test_api_key_value'
    
    try:
        with open('mentor/prompt_config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # Verifica se a configuração aponta para a variável correta
        assert config['llm']['api_key_env'] == 'OPENAI_API_KEY'
        
        # Simula leitura da variável (não testa a API real)
        api_key = os.environ.get(config['llm']['api_key_env'])
        assert api_key == 'test_api_key_value'
    finally:
        # Restaura o valor original
        if original_key is not None:
            os.environ['OPENAI_API_KEY'] = original_key
        else:
            del os.environ['OPENAI_API_KEY']

def test_config_no_hardcoded_secrets():
    """Testa se não há segredos hardcoded no arquivo de configuração."""
    with open('mentor/prompt_config.yaml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se não há chaves de API hardcoded (exemplo: chaves que começam com 'sk-')
    assert 'sk-' not in content
    assert 'AIza' not in content  # Para Google API keys
    
    # Verifica se usa variáveis de ambiente
    assert 'OPENAI_API_KEY' in content  # Está no api_key_env, que é correto
