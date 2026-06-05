[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "carrier_Claims_raw txt_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "File", TransformationQueryName = "carrier_Claims_raw txt_DataDestinationTransform"]]]}]
shared #"carrier_Claims_raw txt" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "5e57f493-2162-43a2-bdf8-35ff9072d4dc"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "f14b66fd-2100-4c98-9025-b73f1aeb0b0a"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "carrier_Claims_raw.txt"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 3", [Delimiter = ",", Columns = 6, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"claim_id", type text}, {"carrier_id", type text}, {"claim_date", type date}, {"amount", Int64.Type}, {"status", type text}, {"adjuster_id", type text}}),
  #"Filtered rows" = Table.SelectRows(#"Changed column type", each ([status] <> "Disputed")),
  #"Added custom" = Table.AddColumn(#"Filtered rows", "claim_category", each if [amount] >= 15000 then "High Value" else "Standard"),
  #"Renamed columns" = Table.RenameColumns(#"Added custom", {{"claim_id", "claim_key"}})
in
  #"Renamed columns";
shared #"carrier_Claims_raw txt (2)" = let
  Source = Lakehouse.Contents(null),
  Navigation = Source{[workspaceId = "5e57f493-2162-43a2-bdf8-35ff9072d4dc"]}[Data],
  #"Navigation 1" = Navigation{[lakehouseId = "f14b66fd-2100-4c98-9025-b73f1aeb0b0a"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Name = "carrier_Claims_raw.txt"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 3", [Delimiter = ",", Columns = 6, QuoteStyle = QuoteStyle.None])
in
  #"Imported CSV";
shared #"carrier_Claims_raw txt_DataDestination" = let
  Pattern = Lakehouse.Contents([CreateNavigationProperties = false, EnableFolding = false, HierarchicalNavigation = true, EnableVorder = true, OutputMetadataRefresh = true]),
  Navigation_1 = Pattern{[workspaceId = "5e57f493-2162-43a2-bdf8-35ff9072d4dc"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "228aba6b-7bb4-4d3a-98e3-a5400824f550"]}[Data],
  Navigation_3 = Navigation_2{[Id = "Files", ItemKind = "Folder"]}[Data],
  FileNavigation = Navigation_3{[Name = "carrier_Claims_raw txt.csv"]}?[Content]?
in
  FileNavigation;
shared #"carrier_Claims_raw txt_DataDestinationTransform" = Csv.OutputConfiguration([Encoding = 65001, Delimiter = ","]);
