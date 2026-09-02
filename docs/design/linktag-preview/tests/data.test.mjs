import test from 'node:test';
import assert from 'node:assert/strict';
import { parseConnections, filterPeople, initialPeople, initialTags } from '../src/data.js';
test('matches roles case insensitively', () => { assert.equal(filterPeople(initialPeople, initialTags).length, 5); assert.equal(filterPeople(initialPeople, ['software engineer']).length, 2); assert.equal(filterPeople(initialPeople, []).length, 0); assert.equal(filterPeople(initialPeople, ['Recruiter']).length, 0); });
test('reads LinkedIn preambles and quoted fields', () => { const people = parseConnections('Notes:\nExported connections\n\nFirst Name,Last Name,Email Address,Company,Position\nMaya,Chen,maya@example.com,"Northstar, Inc.",Software Engineer\n'); assert.equal(people.length, 1); assert.equal(people[0].company, 'Northstar, Inc.'); });
test('supports BOM, CRLF, multiline cells and escaped quotes', () => { const [person] = parseConnections('\uFEFFFirst Name,Last Name,Company,Position\r\nMaya,Chen,"A ""great""\ncompany",UX Designer'); assert.equal(person.company, 'A "great"\ncompany'); });
test('rejects missing headers, incomplete columns, empty data and broken quotes', () => { for (const csv of ['a,b\n1,2', 'First Name,Position\nMaya,Engineer', 'First Name,Last Name,Company,Position', '"unfinished']) assert.throws(() => parseConnections(csv)); });
