
# Naming Conventions

## Purpose

This document defines the naming standards used throughout the Enterprise Market Analytics Platform (EMAP).

The objective is consistency, readability, and maintainability.

---

# General Rules

- Use lowercase letters.
- Separate words using underscores (_).
- Avoid spaces.
- Avoid abbreviations unless standardized.
- Use meaningful names.

Example:

✅ br_stock_price

❌ StockPrice

❌ tbl1

---

# Git Repository

emap-platform

---

# Branches

main

develop

feature/<feature-name>

bugfix/<bug-name>

hotfix/<issue-name>

release/v1.0

---

# Fabric Workspaces

emap-dev

emap-test

emap-prod

---

# Lakehouses

lh_bronze

lh_silver

lh_gold

lh_control

---

# Warehouse

wh_reporting

---

# Pipelines

pl_ingest_rest

pl_bronze_to_silver

pl_silver_to_gold

pl_snapshot

pl_reconciliation

---

# Notebooks

nb_ingest_rest

nb_bronze_to_silver

nb_data_quality

nb_snapshot

---

# Bronze Tables

br_stock_price

br_news

br_company

---

# Silver Tables

sl_stock_price

sl_news

sl_company

---

# Gold Tables

gd_stock_summary

gd_daily_returns

gd_portfolio

gd_sentiment

---

# Views

vw_stock_summary

vw_sector_performance

---

# Stored Procedures

usp_load_metadata

usp_update_watermark

usp_reconciliation

---

# SQL Functions

fn_calculate_rsi

fn_convert_timezone

---

# Triggers

trg_insert_audit

trg_update_history

---

# Azure Functions

func_stock_api

func_news_api

---

# Azure Key Vault

kv_emap_dev

---

# Secrets

secret_yahoo_api

secret_news_api

secret_openai

---

# Parameters

p_source_name

p_load_type

p_run_id

p_target_table

---

# Variables

v_current_date

v_row_count

v_error_message

---

# Audit Tables

audit_pipeline_run

audit_data_quality

audit_reconciliation

---

# Control Tables

ctl_source_system

ctl_pipeline_config

ctl_watermark

ctl_column_mapping
