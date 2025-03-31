insert into Regione(Id,Denominazione,IdRipartizione)
SELECT distinct [Codice Regione]
				,[Denominazione Regione]
				,[Codice Ripartizione Geografica]
FROM [Istat2015].[dbo].[import]
select * from Regione;
insert into Provincia(Id,Denominazione,Sigla,IdRegione)
SELECT distinct [Codice Provincia (Storico)(1)]
,[Denominazione dell'Unità territoriale sovracomunale _(valida a f]
,[Sigla automobilistica]
,[Codice Regione]
  FROM [Istat2015].[dbo].[import]
  order by [Codice Provincia (Storico)(1)]
  insert into Comune(Denominazione,CodiceCatastale,Capoluogo,IdProvincia)
SELECT distinct 
      [Denominazione in italiano]
      ,[Codice Catastale del comune]
	  ,[Flag Comune capoluogo di provincia/città metropolitana/libero co]
      ,[Codice Provincia (Storico)(1)]
  FROM [Istat2015].[dbo].[import]
  order by [Codice Provincia (Storico)(1)]
