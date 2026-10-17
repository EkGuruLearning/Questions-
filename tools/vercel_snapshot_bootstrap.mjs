/* Initial direct-upload deployment when the Vercel GitHub app lacks repo access.
   This bootstrap contains no credentials. Only the exact public commit named in
   EKGURU_SOURCE_SHA is fetched; it never follows an unpinned moving branch. */
import fs from "node:fs/promises";
import { createWriteStream } from "node:fs";
import { Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import { execFileSync } from "node:child_process";

const sha = process.env.EKGURU_SOURCE_SHA || "";
if (!/^[0-9a-f]{40}$/.test(sha)) throw new Error("Set EKGURU_SOURCE_SHA to the exact public, reviewed commit SHA");
await fs.mkdir(".cache", { recursive: true });
const archive = ".cache/ekguru-source.tgz";
const response = await fetch(`https://codeload.github.com/EkGuruLearning/Questions-/tar.gz/${sha}`, { signal: AbortSignal.timeout(180000) });
if (!response.ok || !response.body) throw new Error(`GitHub snapshot download failed (${response.status})`);
await pipeline(Readable.fromWeb(response.body), createWriteStream(archive));
execFileSync("tar", ["-xzf", archive, "--strip-components=1", "--no-same-owner", "--no-same-permissions"], { stdio: "inherit" });
await fs.unlink(archive);
execFileSync("npm", ["ci"], { stdio: "inherit" });
execFileSync("npm", ["run", "build"], { stdio: "inherit" });
