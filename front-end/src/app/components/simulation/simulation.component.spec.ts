import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SimulationComponent } from './simulation.component';
import {MatSidenavModule} from "@angular/material/sidenav";
import {CUSTOM_ELEMENTS_SCHEMA} from "@angular/core";
import {RouterTestingModule} from "@angular/router/testing";
import {HttpClientTestingModule} from "@angular/common/http/testing";
import {BrowserAnimationsModule} from "@angular/platform-browser/animations";
import {MatListModule} from "@angular/material/list";

describe('SimulationComponent', () => {
  let component: SimulationComponent;
  let fixture: ComponentFixture<SimulationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [MatSidenavModule, RouterTestingModule, HttpClientTestingModule, BrowserAnimationsModule, MatListModule],
      declarations: [ SimulationComponent ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SimulationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
