CREATE TABLE IF NOT EXISTS services (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  owner_team TEXT,
  repo TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

DO $$ BEGIN
  CREATE TYPE severity AS ENUM ('low','medium','high','critical');
EXCEPTION
  WHEN duplicate_object THEN null;
END $$;

CREATE TABLE IF NOT EXISTS vulns (
  id BIGSERIAL PRIMARY KEY,
  source TEXT NOT NULL,           -- ZAP | SNYK | SONAR
  service TEXT NOT NULL,
  vuln_id TEXT,
  title TEXT,
  severity severity NOT NULL,
  discovered_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  fixed_at TIMESTAMPTZ,
  url TEXT,
  raw JSONB,
  UNIQUE (source, service, vuln_id, url)
);

CREATE MATERIALIZED VIEW IF NOT EXISTS mv_mttr AS
SELECT service,
       severity,
       AVG(EXTRACT(EPOCH FROM (fixed_at - discovered_at)) / 86400.0) AS mttr_days
FROM vulns
WHERE fixed_at IS NOT NULL
GROUP BY service, severity;
