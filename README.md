# GitFlow Simplificado

Este projeto segue o modelo Simplified GitFlow, ideal para organização e controle de versões ao trabalhar sozinho.

## Sumário

- [Branches Principais](#branches-principais)
- [Branches Temporárias](#branches-temporárias)
- [Fluxo de Trabalho](#fluxo-de-trabalho)
  - [1. Configurar o Projeto](#1-configurar-o-projeto)
  - [2. Trabalhar em uma Funcionalidade](#2-trabalhar-em-uma-funcionalidade)
  - [3. Finalizar a Funcionalidade](#3-finalizar-a-funcionalidade)
  - [4. Preparar uma Versão](#4-preparar-uma-versão)
  - [5. Finalizar a Versão](#5-finalizar-a-versão)
  - [6. Correção Rápida em Produção](#6-correção-rápida-em-produção)
- [Considerações Finais](#considerações-finais)

## Branches Principais

- **master/main**: Contém a versão de produção do software.
- **develop**: Área de desenvolvimento ativo onde novas funcionalidades são integradas.

## Branches Temporárias

- **feature/**: Para desenvolver novas funcionalidades.
- **release/**: Para preparar uma nova versão.
- **hotfix/**: Para correções urgentes em produção.

## Fluxo de Trabalho

### 1. Configurar o Projeto

- **Iniciar develop**: Crie a branch `develop` se ela ainda não existir.

    ```bash
    git checkout -b develop
    git push -u origin develop

### 2. Trabalhar em uma Funcionalidade

- **Criar branch feature**: Use uma nova branch para cada funcionalidade.

    ```bash
    git checkout -b feature/nome-da-feature

- **Desenvolver e integrar**:

    ```bash
    git add .
    git commit -m "feat: Descrição da funcionalidade"
    git push origin feature/nome-da-feature

### 4. Preparar uma Versão

- **Criar branch release**:

    ```bash
    git checkout -b release/x.y.z
    git push origin release/x.y.z

## 5. Finalizar a Versão

- **Mesclar em master e develop**:

    ```bash
    git checkout master
    git merge release/x.y.z
    git push origin master

    git checkout develop
    git merge release/x.y.z
    git push origin develop

    git branch -d release/x.y.z
    git push origin --delete release/x.y.z

- **Criar tag**:

    ```bash
    git tag -a vX.Y.Z -m "Versão X.Y.Z"
    git push origin vX.Y.Z

## 6. Correção Rápida em Produção

- **Criar branch hotfix**:

    ```bash
    git checkout -b hotfix/nome-do-hotfix master
    git add .
    git commit -m "fix: Descrição do hotfix"
    git push origin hotfix/nome-do-hotfix

- **Mesclar em master e develop**:

    ```bash
    git checkout master
    git merge hotfix/nome-do-hotfix
    git push origin master

    git tag -a vX.Y.Z+1 -m "Hotfix: Descrição"
    git push origin vX.Y.Z+1

    git checkout develop
    git merge hotfix/nome-do-hotfix
    git push origin develop

    git branch -d hotfix/nome-do-hotfix
    git push origin --delete hotfix/nome-do-hotfix

## Considerações Finais

Este fluxo simplificado ajuda a manter a organização e clareza no desenvolvimento, permitindo um controle eficiente das versões e correções, mesmo ao trabalhar sozinho. Siga essas práticas para garantir que seu projeto permaneça consistente e fácil de gerenciar.

