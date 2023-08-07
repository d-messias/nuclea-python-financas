-- ATENÇÃO: DELETE/UPDATE SEMPRE USAR WHERE!!!

UPDATE public.cliente
	SET rg= '"25.345.678-1"'
	WHERE cliente.id = 5;