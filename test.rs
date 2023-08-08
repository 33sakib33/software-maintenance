use std::fs::File;

use flate2::Compression;
/* Multi
    line
        comment
            will be removed*/
use flate2::write::GZEncoder;
// Same comment
fn main() -> Result<(), std::io::Error>{

let gz = File::create("archive.tar.gz"); // heere is a comment

let encoder = GZEncoder::new(gz, Compression::default());

let mut tar = tar::Builder::new(enc);

// add all files in the current directory to current_backup

tar.append_dir_all(".", "current_backup")?;

Ok(());
