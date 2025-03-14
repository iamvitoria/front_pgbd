CREATE TABLE `django_migrations` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app` varchar(255) NOT NULL, `name` varchar(255) NOT NULL, `applied` TIMESTAMP NOT NULL)

CREATE TABLE sqlite_sequence(name,seq)

CREATE TABLE `django_content_type` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `app_label` varchar(100) NOT NULL, `model` varchar(100) NOT NULL)

CREATE UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` ON `django_content_type` (`app_label`, `model`)

CREATE TABLE `auth_group_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `group_id` integer NOT NULL REFERENCES `auth_group` (`id`) , `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`) )

CREATE UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `auth_group_permissions` (`group_id`, `permission_id`)

CREATE INDEX `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (`group_id`)

CREATE INDEX `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (`permission_id`)

CREATE TABLE `auth_permission` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `content_type_id` integer NOT NULL REFERENCES `django_content_type` (`id`) , `codename` varchar(100) NOT NULL, `name` varchar(255) NOT NULL)

CREATE UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` ON `auth_permission` (`content_type_id`, `codename`)

CREATE INDEX `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (`content_type_id`)

CREATE TABLE `auth_group` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `name` varchar(150) NOT NULL UNIQUE)

CREATE TABLE `usuario_usuario_groups` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `usuario_id` bigint NOT NULL REFERENCES `usuario_usuario` (`id`) , `group_id` integer NOT NULL REFERENCES `auth_group` (`id`) )

CREATE TABLE `usuario_usuario_user_permissions` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `usuario_id` bigint NOT NULL REFERENCES `usuario_usuario` (`id`) , `permission_id` integer NOT NULL REFERENCES `auth_permission` (`id`) )

CREATE UNIQUE INDEX `usuario_usuario_groups_usuario_id_group_id_a4cfb0b8_uniq` ON `usuario_usuario_groups` (`usuario_id`, `group_id`)

CREATE INDEX `usuario_usuario_groups_usuario_id_62de76a1` ON `usuario_usuario_groups` (`usuario_id`)

CREATE INDEX `usuario_usuario_groups_group_id_b9c090f8` ON `usuario_usuario_groups` (`group_id`)

CREATE UNIQUE INDEX `usuario_usuario_user_permissions_usuario_id_permission_id_c0a85055_uniq` ON `usuario_usuario_user_permissions` (`usuario_id`, `permission_id`)

CREATE INDEX `usuario_usuario_user_permissions_usuario_id_5969a193` ON `usuario_usuario_user_permissions` (`usuario_id`)

CREATE INDEX `usuario_usuario_user_permissions_permission_id_5cad0a4b` ON `usuario_usuario_user_permissions` (`permission_id`)

CREATE TABLE `django_admin_log` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `object_id` VARCHAR(255) NULL, `object_repr` varchar(200) NOT NULL, `action_flag` smallint unsigned NOT NULL CHECK (`action_flag` >= 0), `change_message` VARCHAR(255) NOT NULL, `content_type_id` integer NULL REFERENCES `django_content_type` (`id`) , `user_id` bigint NOT NULL REFERENCES `usuario_usuario` (`id`) , `action_time` TIMESTAMP NOT NULL)

CREATE INDEX `django_admin_log_content_type_id_c4bce8eb` ON `django_admin_log` (`content_type_id`)

CREATE INDEX `django_admin_log_user_id_c564eba6` ON `django_admin_log` (`user_id`)

CREATE TABLE `restaurante_restaurante` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `nome` varchar(100) NOT NULL, `campus` varchar(100) NOT NULL, `ativo` bool NOT NULL)

CREATE TABLE `restaurante_restaurante_refeicoes_oferecidas` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `restaurante_id` bigint NOT NULL REFERENCES `restaurante_restaurante` (`id`) , `refeicao_id` bigint NOT NULL REFERENCES `restaurante_refeicao` (`id`) )

CREATE TABLE `restaurante_cardapiorestaurante` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `data_oferecida` date NOT NULL, `cardapio_id` bigint NOT NULL REFERENCES `cardapio_cardapio` (`id`) , `restaurante_id` bigint NOT NULL REFERENCES `restaurante_restaurante` (`id`) )

CREATE UNIQUE INDEX `restaurante_restaurante_refeicoes_oferecidas_restaurante_id_refeicao_id_bc7fc615_uniq` ON `restaurante_restaurante_refeicoes_oferecidas` (`restaurante_id`, `refeicao_id`)

CREATE INDEX `restaurante_restaurante_refeicoes_oferecidas_restaurante_id_01ebfae3` ON `restaurante_restaurante_refeicoes_oferecidas` (`restaurante_id`)

CREATE INDEX `restaurante_restaurante_refeicoes_oferecidas_refeicao_id_18b75aca` ON `restaurante_restaurante_refeicoes_oferecidas` (`refeicao_id`)

CREATE INDEX `restaurante_cardapiorestaurante_cardapio_id_2669c196` ON `restaurante_cardapiorestaurante` (`cardapio_id`)

CREATE INDEX `restaurante_cardapiorestaurante_restaurante_id_1d00323a` ON `restaurante_cardapiorestaurante` (`restaurante_id`)

CREATE TABLE `cardapio_cardapio` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `principal` VARCHAR(255) NOT NULL, `acompanhamento` VARCHAR(255) NOT NULL, `bebidas` VARCHAR(255) NOT NULL, `refeicao_id` bigint NOT NULL REFERENCES `restaurante_refeicao` (`id`) )

CREATE INDEX `cardapio_cardapio_refeicao_id_a9001ebf` ON `cardapio_cardapio` (`refeicao_id`)

CREATE TABLE `financeiro_carteira` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `saldo` real NOT NULL, `usuario_id` bigint NOT NULL REFERENCES `usuario_usuario` (`id`) )

CREATE INDEX `financeiro_carteira_usuario_id_f3355fb4` ON `financeiro_carteira` (`usuario_id`)

CREATE TABLE `financeiro_transacao` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `valor` real NOT NULL, `data` TIMESTAMP NOT NULL, `is_entrada` bool NOT NULL, `carteira_id` bigint NOT NULL REFERENCES `financeiro_carteira` (`id`) )

CREATE INDEX `financeiro_transacao_carteira_id_0a2db9a8` ON `financeiro_transacao` (`carteira_id`)

CREATE TABLE `django_session` (`session_key` varchar(40) NOT NULL PRIMARY KEY, `session_data` VARCHAR(255) NOT NULL, `expire_date` TIMESTAMP NOT NULL)

CREATE INDEX `django_session_expire_date_a5c62663` ON `django_session` (`expire_date`)

CREATE TABLE `agendamento_agendamento` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `data_agendamento` TIMESTAMP NOT NULL, `is_fila_espera` bool NOT NULL, `cardapio_agendado_id` bigint NOT NULL REFERENCES `restaurante_cardapiorestaurante` (`id`) , `usuario_id` bigint NOT NULL REFERENCES `usuario_usuario` (`id`) , `checkin` bool NOT NULL, `posicao_fila` integer NULL, `ativo` bool NOT NULL)

CREATE INDEX `agendamento_agendamento_cardapio_agendado_id_007231ae` ON `agendamento_agendamento` (`cardapio_agendado_id`)

CREATE INDEX `agendamento_agendamento_usuario_id_54e30ffe` ON `agendamento_agendamento` (`usuario_id`)

CREATE TABLE `restaurante_refeicao` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `nome` varchar(100) NOT NULL, `horario_abertura` time NOT NULL, `horario_fechamento` time NOT NULL, `valor` decimal NOT NULL, `ativo` bool NOT NULL, `limite_agendamentos` integer NOT NULL)

CREATE TABLE `usuario_usuario` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `password` varchar(128) NOT NULL, `last_login` TIMESTAMP NULL, `is_superuser` bool NOT NULL, `is_staff` bool NOT NULL, `is_active` bool NOT NULL, `date_joined` TIMESTAMP NOT NULL, `nome_completo` varchar(100) NOT NULL, `email` varchar(254) NOT NULL UNIQUE, `cpf` varchar(14) NULL UNIQUE, `telefone` varchar(11) NULL, `data_nascimento` date NULL, `matricula` varchar(10) NULL, `imagem` varchar(100) NOT NULL, CONSTRAINT `valid_cpf_format` CHECK (`cpf` REGEXP '^\d{3}\.\d{3}\.\d{3}-\d{2}$'), CONSTRAINT `valid_telefone_format` CHECK (`telefone` REGEXP '^\d{11}$'), CONSTRAINT `valid_matricula_format` CHECK (`matricula` REGEXP '^\d{9}$'))

CREATE TABLE `usuario_preferencias` (`id` integer NOT NULL PRIMARY KEY AUTO_INCREMENT, `comidas_favoritas` VARCHAR(255) NOT NULL, `usuario_id` bigint NOT NULL UNIQUE REFERENCES `usuario_usuario` (`id`) , `onivoro` bool NOT NULL, `vegetariano` bool NOT NULL)